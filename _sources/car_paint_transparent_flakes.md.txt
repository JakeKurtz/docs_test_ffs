# Chameleon Paint w. Transparent Flakes

Has the same three layers (base coat, flakes, and a clear top coat), where the flakes are transparent and coated with a thinfilm.

<img src="_images/c_trans_flakes.png" alt="my alt text" width="50%"/>

## Inputs

### Base Coat

#### Color
Specifies the base color of the paint.
<figure>
  <img src="_images/bc_color/strip.png" alt="my alt text"/>
  <figcaption text-align="center">Variation of base colors</figcaption>
</figure>

#### Metallic
Controls the metallic appearance of the base paint coat.
<figure>
  <img src="_images/bc_metal/strip.png" alt="my alt text"/>
  <figcaption text-align="center">Metallic from 0.0 to 1.0</figcaption>
</figure>

#### Specular Tint
Adjusts the tint of the specular highlights.
<figure>
  <img src="_images/bc_spec_tint/strip.png" alt="my alt text"/>
  <figcaption text-align="center">From white to orange</figcaption>
</figure>

#### Roughness
Controls the roughness of the base paint coat.
<figure>
  <img src="_images/bc_roughness/strip.png" alt="my alt text"/>
  <figcaption text-align="center">Roughness from 0.0 to 1.0</figcaption>
</figure>

### Flakes Coat

#### Scale
Adjusts the size of the flakes.
<figure>
  <img src="_images/flake_trans_scale/strip.png" alt="my alt text"/>
  <figcaption text-align="center">Scale from 250.0 to 5000.0</figcaption>
</figure>

#### Density
Controls the density of the flakes.
<figure>
  <img src="_images/flake_trans_density/strip.png" alt="my alt text"/>
  <figcaption text-align="center">Density from 0.0 to 1.0</figcaption>
</figure>

#### Variation
This parameter determines the extent to which flake orientation deviates from the surface normal. A value of 0.0 means minimal deviation, aligning flakes closely with the surface. Higher values intensify the flake effect, making it more pronounced.
<figure>
  <img src="_images/flake_trans_var/strip.png" alt="my alt text"/>
  <figcaption text-align="center">Variation from 0.0 to 0.3</figcaption>
</figure>

#### Roughness
Specifies the roughness of the flakes.
<figure>
  <img src="_images/flake_trans_roughness/strip.png" alt="my alt text"/>
  <figcaption text-align="center">Roughness from 0.0 to 1.0</figcaption>
</figure>

#### Absorption
Specifies the degree of light absorbed by the pigment before it is reflected off the flakes.
<figure>
  <img src="_images/flake_trans_absorption/strip.png" alt="my alt text"/>
  <figcaption text-align="center">Absorption from 1.0 to 10.0, with a red base coat</figcaption>
</figure>

#### Weight
This multiplier scales the reflection intensity received by the flakes.
<figure>
  <img src="_images/flake_trans_weight/strip.png" alt="my alt text"/>
  <figcaption text-align="center">Weight from 0.0 to 1.0</figcaption>
</figure>

### Flakes Film

#### IOR and Thickness

<div class="video_container">
    <figure>
        <video width="100%" height="auto" controls loop>
            <source src="_images/flake_trans_ior/vid.mp4" type="video/mp4">
        </video>
        <figcaption text-align="center">Film IOR from 1.0 to 3.0</figcaption>
    </figure>
    <figure>
        <video width="100%" height="auto" controls loop>
            <source src="_images/flake_trans_thickness/vid.mp4" type="video/mp4">
        </video>
        <figcaption text-align="center">Film thickness from 0.0nm to 800.0nm</figcaption>
    </figure>
</div>

#### Variance
Controls the variance of the flake film thickness. Lower values are dull and desaturated, higher values are bright and saturated. 
<figure>
  <img src="_images/flake_trans_film_var/strip.png" alt="my alt text"/>
  <figcaption text-align="center">Variance from 0.0 to 50.0</figcaption>
</figure>

### Clear Coat

#### Color
Specifies the color of the clear coat layer.
<figure>
  <img src="_images/cc_color/strip.png" alt="my alt text"/>
  <figcaption text-align="center">Color from black to white</figcaption>
</figure>

#### Roughness
Controls the roughness of the clear coat layer.
<figure>
  <img src="_images/cc_roughness/strip.png" alt="my alt text"/>
  <figcaption text-align="center">Roughness from 0.0 to 1.0</figcaption>
</figure>

## Outputs

### Shader
Standard shader output.