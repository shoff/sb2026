"""
Shader Manager - Compiles and manages GLSL shaders.
"""

from OpenGL.GL import *
import numpy as np
from pathlib import Path
from typing import Dict, Optional


class ShaderProgram:
    """
    Wrapper for an OpenGL shader program.
    """

    def __init__(self, program_id: int):
        self.program_id = program_id
        self.uniform_locations: Dict[str, int] = {}

    def use(self):
        """Activate this shader program."""
        glUseProgram(self.program_id)

    def get_uniform_location(self, name: str) -> int:
        """
        Get uniform location, cached.

        Args:
            name: Uniform name

        Returns:
            Uniform location
        """
        if name not in self.uniform_locations:
            self.uniform_locations[name] = glGetUniformLocation(self.program_id, name)
        return self.uniform_locations[name]

    def set_mat4(self, name: str, matrix: np.ndarray):
        """Set a 4x4 matrix uniform."""
        loc = self.get_uniform_location(name)
        if loc != -1:
            glUniformMatrix4fv(loc, 1, GL_FALSE, matrix.T)  # Transpose for OpenGL column-major

    def set_vec3(self, name: str, vec: np.ndarray):
        """Set a vec3 uniform."""
        loc = self.get_uniform_location(name)
        if loc != -1:
            glUniform3fv(loc, 1, vec)

    def set_float(self, name: str, value: float):
        """Set a float uniform."""
        loc = self.get_uniform_location(name)
        if loc != -1:
            glUniform1f(loc, value)

    def set_int(self, name: str, value: int):
        """Set an int uniform."""
        loc = self.get_uniform_location(name)
        if loc != -1:
            glUniform1i(loc, value)

    def set_bool(self, name: str, value: bool):
        """Set a bool uniform."""
        loc = self.get_uniform_location(name)
        if loc != -1:
            glUniform1i(loc, 1 if value else 0)

    def delete(self):
        """Delete shader program."""
        if self.program_id:
            glDeleteProgram(self.program_id)
            self.program_id = 0


class ShaderManager:
    """
    Manages compilation and caching of shader programs.
    """

    def __init__(self):
        self.programs: Dict[str, ShaderProgram] = {}
        self.shader_dir = Path(__file__).parent / "shaders"

    def load_shader(self, name: str, vert_file: str, frag_file: str) -> Optional[ShaderProgram]:
        """
        Load and compile a shader program.

        Args:
            name: Shader program name
            vert_file: Vertex shader filename
            frag_file: Fragment shader filename

        Returns:
            ShaderProgram or None on error
        """
        if name in self.programs:
            return self.programs[name]

        # Read shader source files
        vert_path = self.shader_dir / vert_file
        frag_path = self.shader_dir / frag_file

        if not vert_path.exists():
            print(f"Vertex shader not found: {vert_path}")
            return None
        if not frag_path.exists():
            print(f"Fragment shader not found: {frag_path}")
            return None

        with open(vert_path, 'r') as f:
            vert_source = f.read()
        with open(frag_path, 'r') as f:
            frag_source = f.read()

        # Compile shaders
        vert_shader = self._compile_shader(vert_source, GL_VERTEX_SHADER, vert_file)
        if not vert_shader:
            return None

        frag_shader = self._compile_shader(frag_source, GL_FRAGMENT_SHADER, frag_file)
        if not frag_shader:
            glDeleteShader(vert_shader)
            return None

        # Link program
        program_id = glCreateProgram()
        glAttachShader(program_id, vert_shader)
        glAttachShader(program_id, frag_shader)
        glLinkProgram(program_id)

        # Check link status
        if not glGetProgramiv(program_id, GL_LINK_STATUS):
            error = glGetProgramInfoLog(program_id).decode()
            print(f"Shader program link error ({name}):\n{error}")
            glDeleteProgram(program_id)
            glDeleteShader(vert_shader)
            glDeleteShader(frag_shader)
            return None

        # Clean up shader objects (no longer needed after linking)
        glDeleteShader(vert_shader)
        glDeleteShader(frag_shader)

        # Create shader program wrapper
        program = ShaderProgram(program_id)
        self.programs[name] = program

        print(f"Shader program '{name}' compiled successfully")
        return program

    def _compile_shader(self, source: str, shader_type: int, filename: str) -> Optional[int]:
        """
        Compile a shader from source.

        Args:
            source: Shader source code
            shader_type: GL_VERTEX_SHADER or GL_FRAGMENT_SHADER
            filename: Filename for error reporting

        Returns:
            Shader ID or None on error
        """
        shader = glCreateShader(shader_type)
        glShaderSource(shader, source)
        glCompileShader(shader)

        # Check compile status
        if not glGetShaderiv(shader, GL_COMPILE_STATUS):
            error = glGetShaderInfoLog(shader).decode()
            shader_type_str = "vertex" if shader_type == GL_VERTEX_SHADER else "fragment"
            print(f"{shader_type_str.capitalize()} shader compile error ({filename}):\n{error}")
            glDeleteShader(shader)
            return None

        return shader

    def get(self, name: str) -> Optional[ShaderProgram]:
        """
        Get a shader program by name.

        Args:
            name: Shader program name

        Returns:
            ShaderProgram or None if not found
        """
        return self.programs.get(name)

    def cleanup(self):
        """Delete all shader programs."""
        for program in self.programs.values():
            program.delete()
        self.programs.clear()
