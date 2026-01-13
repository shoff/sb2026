#version 330 core

// Vertex attributes
layout(location = 0) in vec3 aPosition;
layout(location = 1) in vec3 aNormal;
layout(location = 2) in vec2 aTexCoord;

// Uniforms
uniform mat4 uModel;
uniform mat4 uView;
uniform mat4 uProjection;
uniform mat4 uNormalMatrix;

// Outputs to fragment shader
out vec3 vFragPos;
out vec3 vNormal;
out vec2 vTexCoord;

void main() {
    // Transform position
    vec4 worldPos = uModel * vec4(aPosition, 1.0);
    vFragPos = worldPos.xyz;

    // Transform normal
    vNormal = mat3(uNormalMatrix) * aNormal;

    // Pass through texture coordinates
    vTexCoord = aTexCoord;

    // Final position
    gl_Position = uProjection * uView * worldPos;
}
