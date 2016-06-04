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


/*this is the only part of the default shader we need to change 
  to grayscale our kitten: we need to take the average of the rgb 
  channels and then assign rgb to be the average */
void main (void){
        
        if(is_active > 0. ) {
                vec2 onePixel = vec2(1.0 / 480.0, 1.0 / 320.0);
                vec2 texCoord = tex_coord0;
                texCoord.x += sin(u_time) * (onePixel.x * 6.0);
                texCoord.y += cos(u_time) * (onePixel.y * 6.0);
                vec4 color;
                color.rgb = vec3(0.5);
                color -= texture2D(texture0, texCoord - onePixel) * 5.0;
                color += texture2D(texture0, texCoord + onePixel) * 5.0;
                color.rgb = vec3(color.r + color.g + color.b) / 3.0;
                gl_FragColor = vec4(color.rgb, 1);
        } else {
                vec4 pixel_color = frag_color * texture2D(texture0, tex_coord0);
                float average = (pixel_color[0] + pixel_color[1] + pixel_color[2])/3.;
                gl_FragColor = vec4(pixel_color);
        }
}
