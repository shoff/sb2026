#version 330 core

// Vertex attributes
layout(location = 0) in vec3 aPosition;
layout(location = 1) in vec3 aNormal;
layout(location = 2) in vec2 aTexCoord;
layout(location = 3) in vec4 aBoneIndices;  // Up to 4 bones per vertex
layout(location = 4) in vec4 aBoneWeights;  // Corresponding weights

// Uniforms
uniform mat4 uBoneMatrices[128];  // Support up to 128 bones
uniform mat4 uModel;
uniform mat4 uView;
uniform mat4 uProjection;
uniform mat4 uNormalMatrix;
uniform bool uUseSkinning;  // Whether to apply skinning

// Outputs to fragment shader
out vec3 vFragPos;
out vec3 vNormal;
out vec2 vTexCoord;

void main() {
    vec4 skinnedPos;
    vec3 skinnedNormal;

    if (uUseSkinning) {
        // Compute skinned position
        skinnedPos = vec4(0.0);
        skinnedNormal = vec3(0.0);

        for (int i = 0; i < 4; i++) {
            int boneIndex = int(aBoneIndices[i]);
            float weight = aBoneWeights[i];

            if (weight > 0.0 && boneIndex >= 0 && boneIndex < 128) {
                mat4 boneTransform = uBoneMatrices[boneIndex];
                skinnedPos += boneTransform * vec4(aPosition, 1.0) * weight;
                skinnedNormal += mat3(boneTransform) * aNormal * weight;
            }
        }
    } else {
        // No skinning - use original position
        skinnedPos = vec4(aPosition, 1.0);
        skinnedNormal = aNormal;
    }

    // Transform to world space
    vec4 worldPos = uModel * skinnedPos;
    vFragPos = worldPos.xyz;

    // Transform normal
    vNormal = normalize(mat3(uNormalMatrix) * skinnedNormal);

    // Pass through texture coordinates
    vTexCoord = aTexCoord;

    // Final position
    gl_Position = uProjection * uView * worldPos;
}
