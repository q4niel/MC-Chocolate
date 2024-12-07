# MC Chocolate
A collection of simple <!---batch/-->shell scripts designed to help you download and install a variety of Minecraft assets from their official sources.
This project does not include any assets themselves, but automates the process of fetching them from the official download sites.

## Install Guide
1. **Prerequisites**:
   The scripts utilizes **curl** for downloads, which should be installed on any relatively modern system.
   Most Linux distributions and macOS have it pre-installed. On Windows, you may need to install it manually.

2. **Download your Script**:
   Refer to each release's release notes for the specific functionality of the provided scripts.
   You can download the scripts from the [releases section](https://github.com/q4niel/MC-Chocolate/releases).
   Please refer to the release notes for specific functionality and changes in each version.

3. **Run your Script**:
    - After downloading, execute the script in a terminal or command prompt from the directory where the script is located.
    - The script will create a new directory in the current working directory.
    - The new directory will contain all the downloaded assets including **datapacks**, **shaderpacks**, **resourcepacks**, and **mods**.
    ```
    /MC-Chocolate-XXX-XXX/
        ├── datapacks/
        ├── shaderpacks/
        ├── resourcepacks/
        ├── mods/
    ```

## Licensing
This project does not have a license.
It does not distribute any **datapacks**, **shaderpacks**, **resourcepacks**, or **mods**.
All assets are downloaded directly from their official sources.
Each asset is licensed under its respective license, so please refer to their official websites for licensing terms and usage guidelines.

## Official Asset Sources
These scripts download assets from the following **official sources**. Visit the **links** for more details about each asset and its **licensing**.
- **World Generation**:
    - [Tectonic](https://modrinth.com/datapack/tectonic/version/aLQ1otmd)
    - [Terrestria](https://modrinth.com/mod/terrestria/version/7.0.1)
    - [Geophilic](https://modrinth.com/datapack/geophilic/version/3.1.4)
    - [Tidal Towns](https://modrinth.com/datapack/tidal-towns/version/lMvNx9a5)
- **Quality of Life**:
    - [Mod Menu](https://modrinth.com/mod/modmenu/version/11.0.3)
    - [Simple Voice Chat](https://modrinth.com/plugin/simple-voice-chat/version/fabric-1.21.1-2.5.26)
    - [LambDynamicLights](https://modrinth.com/mod/lambdynamiclights/version/3.1.3+1.21.1)
    - [Model Gap Fix](https://modrinth.com/mod/modelfix/version/1.21-1.6)
    - [Leaves Be Gone](https://modrinth.com/mod/leaves-be-gone/version/v21.0.0-1.21-Fabric)
    - [RightClickHarvest](https://modrinth.com/mod/rightclickharvest/version/4R1YFTOu)
    - [Tool Trims](https://modrinth.com/datapack/tool-trims/version/2.2.2)
    - [Visual Workbench](https://modrinth.com/mod/visual-workbench/version/v21.0.5-1.21-Fabric)
    - [Easy Anvils](https://modrinth.com/mod/easy-anvils/version/v21.0.5-1.21-Fabric)
    - [Easy Magic](https://modrinth.com/mod/easy-magic/version/v21.0.4-1.21-Fabric)
- **Mobs**:
    - [Horse Buff](https://modrinth.com/mod/horsebuff/version/2.1.8)
    - [Cave Spider Spawn](https://modrinth.com/mod/cave-spider-spawn/version/1.21.1-1.2-fabric+forge+neo)
    - [More Babies](https://modrinth.com/mod/more-babies/version/2.0.0-1.21-fabric)
    - [Friends & Foes](https://modrinth.com/mod/friends-and-foes/version/fabric-mc1.21.1-3.0.6)
    - [Nyf's Spiders](https://modrinth.com/mod/nyfs-spiders/version/XrZVRpEA)
    - [More Mob Variants](https://modrinth.com/mod/more-mob-variants/version/1.3.1.1)
    - [Variants & Ventures](https://modrinth.com/mod/variants-and-ventures/version/fabric-mc1.21.1-1.0.6)
    - [Boids](https://modrinth.com/mod/boids/version/1.2.3)
    - [Flourishing Fields](https://github.com/q4niel/Flourishing-Fields/releases/tag/0.2.1)
- **Building**
    - [Items Displayed](https://modrinth.com/mod/items-displayed/version/1.3-1.21)
    - [Connectible Chains](https://modrinth.com/mod/connectiblechains/version/2.4.2+1.21.1)
- **Quirks**
    - [Serene Seasons](https://modrinth.com/mod/serene-seasons/version/q8BN28TQ)
    - [What Are They Up To (Watut)](https://modrinth.com/mod/what-are-they-up-to/version/1.21.0-1.1.3)
    - [Elytra Burn](https://github.com/q4niel/Elytra-Burn/releases/tag/0.0.1)
    - [Primitive Progression](https://github.com/q4niel/Primitive-Progression/releases/tag/0.4.0)
    - [Passive Regen](https://github.com/q4niel/Passive-Regen/releases/tag/0.0.1)
    - [Mending Begone](https://github.com/q4niel/Mending-Begone/releases/tag/0.1.1)
    - [Hunger Fix](https://github.com/q4niel/Hunger-Fix/releases/tag/0.1.0)
    - [Nature's Cauldron](https://github.com/q4niel/Natures-Cauldron/releases/tag/0.2.0)
- **Optimization**
    - [Sodium](https://modrinth.com/mod/sodium/version/mc1.21-0.5.9)
    - [Lithium](https://modrinth.com/mod/lithium/version/mc1.21-0.13.1)
    - [Entity Culling](https://modrinth.com/mod/entityculling/version/MQuJQtw8)
- **Dependencies**
    - [Fabric API](https://modrinth.com/mod/fabric-api/version/0.102.0+1.21)
    - [Cloth Config API](https://modrinth.com/mod/cloth-config/version/15.0.140+fabric)
    - [Text Placeholder API](https://modrinth.com/mod/placeholder-api/version/2.4.1+1.21)
    - [Architectury API](https://modrinth.com/mod/architectury-api/version/13.0.8+fabric)
    - [Puzzles Lib](https://modrinth.com/mod/puzzles-lib/version/v21.0.28-1.21-Fabric)
    - [Forge Config API Port](https://modrinth.com/mod/forge-config-api-port/version/v21.0.8-1.21-Fabric)
    - [JamLib](https://modrinth.com/mod/jamlib/version/GuJVwwK1)
    - [Collective](https://modrinth.com/mod/collective/version/1.21.1-7.87-fabric+forge+neo)
    - [CoroUtil](https://modrinth.com/mod/coroutil/version/1.21.0-1.3.7)
    - [GlitchCore](https://modrinth.com/mod/glitchcore/version/2zGz6n4Q)