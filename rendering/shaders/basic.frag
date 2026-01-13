#version 330 core

// Inputs from vertex shader
in vec3 vFragPos;
in vec3 vNormal;
in vec2 vTexCoord;

// Uniforms
uniform sampler2D uTexture;
uniform bool uHasTexture;
uniform vec3 uLightDir;
uniform vec3 uLightColor;
uniform vec3 uAmbientColor;
uniform vec3 uViewPos;

// Output
out vec4 FragColor;

void main() {
    // Base color
    vec3 baseColor;
    if (uHasTexture) {
        baseColor = texture(uTexture, vTexCoord).rgb;
    } else {
        baseColor = vec3(0.7, 0.7, 0.7);  // Default gray
    }

    // Normalize vectors
    vec3 normal = normalize(vNormal);
    vec3 lightDir = normalize(uLightDir);
    vec3 viewDir = normalize(uViewPos - vFragPos);

    // Ambient lighting
    vec3 ambient = uAmbientColor * baseColor;

    // Diffuse lighting
    float diff = max(dot(normal, lightDir), 0.0);
    vec3 diffuse = diff * uLightColor * baseColor;

    // Specular lighting (Blinn-Phong)
    vec3 halfwayDir = normalize(lightDir + viewDir);
    float spec = pow(max(dot(normal, halfwayDir), 0.0), 32.0);
    vec3 specular = spec * uLightColor * 0.3;

    // Combine lighting
    vec3 result = ambient + diffuse + specular;

    // Output color
    FragColor = vec4(result, 1.0);
}
