# Engine Sim: Generator
An engine generator for the [Engine Simulator](https://github.com/ange-yaghi/engine-sim) by [AngeTheGreat](https://github.com/ange-yaghi).
  
## Warning: Early builds, may not work without updated python libraries.

![es-gen-v0.0.1.gif](https://github.com/aaronslifegame/es-generator/public/es-gen-v0.0.1.gif)
---

# Releases
`0.0.1` - Command line generator.
`0.1.0` - Gui (Coming soon).

# Instructions
for version `0.0.1`:
- start the 'engine.py' (es-generator/es-gen/engine.py).

- Engine Name: Enter the name of your engine.
- Number of Banks: Enter the number of banks you want your engine to have (inline: 1, v/vr/flat: 2, w: 3-4).
  - Number of Cylinders: The number fo cylinder in the bank.
  - Cylinder 0: The order of cylinder on the crankshaft.
  - Bank Angle: the angle of your banks (Anti-clockwise).
  '*' (You may need to do this multiple times depending on the amount of cylinders).
'*' (Repeat, depending on amount of banks (the oder of cylinder is continued from every bank)).
- Done! (Engine configuration 'YOUR-ENGINE' generated and saved to (es-generator/es-gen/engines/YOUR-ENGINE_engine.py)).

More info at [Engine Simulator](https://github.com/aaronslifegame/es-generator/docs/tutorals.md) in the future.
  
# Sources
[Engine Simulator](https://github.com/ange-yaghi/engine-sim)
[Piranha](https://github.com/ange-yaghi/piranha)
[Python Engine Generator](https://github.com/ange-yaghi/engine-generator)
[Enginette](https://github.com/Enginette/enginette)
