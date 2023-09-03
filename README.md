<p align="center"><img src="https://github.com/AaronsLifeGame/es-generator/blob/main/public/es-gen.png" width="250" height="250"></p>

# Engine Simulator: Generator
An engine generator for the [Engine Simulator](https://github.com/ange-yaghi/engine-sim) by [AngeTheGreat](https://github.com/ange-yaghi).
  
## Warning: Early builds, may not work without updated python libraries.

![es-gen-v0.2.1.gif](https://github.com/AaronsLifeGame/es-generator/blob/main/public/es-gen-v0.2.1.gif)
![es-gen-v0.2.1.gif](https://github.com/AaronsLifeGame/es-generator/blob/main/public/es-gen-v0.1.0.gif)
---

## Releases
`v1.0.0` - Gui (Coming soon). \

`v0.3.1` - Added Transmission and Vehicle modification. [Download [Latest Release]](https://github.com/AaronsLifeGame/es-generator/releases/download/v0.3.1/es-gen-v0.3.1.zip) \

`v0.2.3` - Advanced Settings & Firing order + Bug Fixes. [Download](https://github.com/AaronsLifeGame/es-generator/releases/download/v0.2.3/es-gen-v0.2.3.zip) \
`v0.1.0` - Command line generator [Initial release]. [Download](https://github.com/AaronsLifeGame/es-generator/releases/download/v0.1.0/es-gen-v0.1.0.zip) \


## Instructions 0.3.1 [Latest Release]
1. **Prerequisites:**
   - Ensure you have Python installed.

2. **Run the Script:**
   - Open a terminal or command prompt.
   - Navigate to the script's directory.
   - Execute the script with: `python engine.py`.

3. **Basic Configuration:**
   - Input engine name.
   - Enter the number of banks.
   - For each bank:
   - enter the number of cylinders.
   - Specify the cylinder order (starting from 0) for each bank.
   - Specify bank angle (positive goes anti-clockwise).
   - Choose whether to flip each bank.

4. **Firing Order (Optional)r:**
   - If you skip the order will be 1,2,3,4 and so on.
   - Other wise input the firing order for each cylinder (starting from 1).

5. **Advanced Settings (Optional):**
   - Choose if you want to configure advanced settings (you can skip spesific setting just by pressing enter, this will use the default value).
   - Adjust values such as starter torque, redline, etc.
   - [Explanation Here](https://github.com/AaronsLifeGame/es-generator/wiki/Instructions#v020)  

6. **Engine Generation**
   - The generated engine configuration file will be saved in the `engines` folder as a `.mr` file.

7. **Modify Transmisson** 
   - ...

8. **Modify Vehicle**
   - ...

More info at [Wiki Instructions](https://github.com/AaronsLifeGame/es-generator/wiki/Instructions).

## Community/contributors
>- AngeTheGreat
>- DDev
>- Supernalboot
>- Strikkies
>- QuickRushInc
>- LamborghiniEnjoyer
>- Goldwolf
>- ISAK.M
>- FateOri
>- F*ckaroo
  
## Sources
>- [Engine Simulator](https://github.com/ange-yaghi/engine-sim)
>- [Piranha](https://github.com/ange-yaghi/piranha)
>- [Python Engine Generator](https://github.com/ange-yaghi/engine-generator)
>- [Enginette](https://github.com/Enginette/enginette)
