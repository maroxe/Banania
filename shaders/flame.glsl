---VERTEX SHADER---
#ifdef GL_ES
precision highp float;
#endif

/* Outputs to the fragment shader */
varying vec4 frag_color;
varying vec2 tex_coord0;

/* vertex attributes */
attribute vec2     vPosition;
attribute vec2     vTexCoords0;

/* uniform variables */
uniform mat4       modelview_mat;
uniform mat4       projection_mat;
uniform vec4       color;
uniform float      opacity;

void main (void) {
        frag_color = color * vec4(1.0, 1.0, 1.0, opacity);
        tex_coord0 = vTexCoords0;
        gl_Position = projection_mat * modelview_mat * vec4(vPosition.xy, 0.0, 1.0);
}


---FRAGMENT SHADER---
#ifdef GL_ES
precision highp float;
#endif

/* inputs from the vertex shader */
varying vec4 frag_color;
varying vec2 tex_coord0;

/* uniform texture samplers */
uniform sampler2D texture0;

uniform float u_time;
uniform float is_active;
uniform vec2 resolution;

uniform vec2 center; // Mouse position
uniform float time; // effect elapsed time
uniform vec3 shockParams; // 10.0, 0.8, 0.1

void main() 
{ 
        if(is_active > 0. ) {
                vec2 uv = tex_coord0.xy;
                vec2 texCoord = uv;
                float distance = distance(uv, center);
                if ( (distance <= (time + shockParams.z)) && 
                     (distance >= (time - shockParams.z)) ) {
                        float diff = (distance - time); 
                        float powDiff = 1.0 - pow(abs(diff*shockParams.x), 
                                                  shockParams.y); 
                        float diffTime = diff  * powDiff; 
                        vec2 diffUV = normalize(uv - center); 
                        texCoord = uv + (diffUV * diffTime);
                } 
                gl_FragColor = frag_color * texture2D(texture0, texCoord);
        } else {
                vec4 pixel_color = frag_color * texture2D(texture0, tex_coord0);
                float average = (pixel_color[0] + pixel_color[1] + pixel_color[2])/3.;
                gl_FragColor = vec4(pixel_color);
                
        }
}

