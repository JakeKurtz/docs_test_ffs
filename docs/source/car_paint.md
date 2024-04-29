# Basic Paint

Utilizes a three-layer system: base coat, metallic flakes, and a clear top coat.

<img src="_images/basic_paint.png" alt="my alt text" width="50%"/>

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

#### Tint

Sets the color of the flakes tint in the paint.
<figure>
  <img src="_images/flake_tint/strip.png" alt="my alt text"/>
  <figcaption text-align="center">Variation of flake tints, with absorption value of 5.5</figcaption>
</figure>

#### Scale
Adjusts the size of the flakes.
<figure>
  <img src="_images/flake_scale/strip.png" alt="my alt text"/>
  <figcaption text-align="center">Scale from 250.0 to 5000.0</figcaption>
</figure>

#### Density
Controls the density of the flakes.
<figure>
  <img src="_images/flake_density/strip.png" alt="my alt text"/>
  <figcaption text-align="center">Density from 0.0 to 1.0</figcaption>
</figure>

#### Variation
This parameter determines the extent to which flake orientation deviates from the surface normal. A value of 0.0 means minimal deviation, aligning flakes closely with the surface. Higher values intensify the flake effect, making it more pronounced.
<figure>
  <img src="_images/flake_var/strip.png" alt="my alt text"/>
  <figcaption text-align="center">Variation from 0.0 to 0.1</figcaption>
</figure>

#### Roughness
Specifies the roughness of the flakes.
<figure>
  <img src="_images/flake_roughness/strip.png" alt="my alt text"/>
  <figcaption text-align="center">Roughness from 0.0 to 1.0</figcaption>
</figure>

#### Absorption

```{tip}
For realistic results, try using an absorption with a value higher than 0. It gives a better impression of the flakes being embedded in the paint.
```

Specifies the degree of light absorbed by the pigment before it is reflected off the flakes.
<figure>
  <img src="_images/flake_absorption/strip.png" alt="my alt text"/>
  <figcaption text-align="center">Absorption from 1.0 to 30.0</figcaption>
</figure>

#### Weight
This multiplier scales the reflection intensity received by the flakes.
<figure>
  <img src="_images/flake_weight/strip.png" alt="my alt text"/>
  <figcaption text-align="center">Weight from 0.0 to 1.0</figcaption>
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