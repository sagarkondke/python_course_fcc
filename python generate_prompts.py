import itertools
import csv

# 1. Define the components of your prompt architecture
styles = [
    "A minimalist vector logo",
    "Abstract geometric logo",
    "Continuous line logo",
    "A sleek corporate logo",
    "Isometric tech logo"
]

math_concepts = [
    "Costa's minimal surface",
    "E_8 Lie group root system projection",
    "4D quaternion Julia set cross-section",
    "Poincaré disk model tessellation",
    "Clebsch diagonal cubic surface",
    "Hopf fibration mapping",
    "Rössler attractor phase space trajectory",
    "Wolfram's Rule 30 cellular automaton",
    "Calabi-Yau manifold projection",
    "Penrose tiling"
]

parameters = [
    "using precise golden ratio circles",
    "with sharp fractal outer edges",
    "using regular heptagons in hyperbolic space",
    "rendered as a minimalist wireframe",
    "with overlapping transparency effects",
    "creating an asymmetrical dynamic loop"
]

constraints = [
    "Flat design, no gradients",
    "Isometric projection to imply 3D depth on a strict 2D plane",
    "Clean flat design, modern SaaS company aesthetic",
    "Thick line weight, minimalist, modern",
    "Precise geometric pixelation, flat vector"
]

colors = [
    "monochromatic deep blue and gold, clean white background",
    "neon gradient on a dark background",
    "monochromatic black and white",
    "vibrant tech-forward color palette, transparent background",
    "cyan and silver metallic finish",
    "orange and purple gradient vector",
    "high contrast black and neon green"
]

# 2. Generate all possible combinations
# This automatically pairs every item with every other item across the lists
all_combinations = list(itertools.product(styles, math_concepts, parameters, constraints, colors))

# 3. Limit to exactly 1000 prompts
target_amount = 1000
final_prompts = all_combinations[:target_amount]

# 4. Save to a CSV file for easy copy-pasting
filename = "1000_Math_Abstract_Logos.csv"
with open(filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["AI Prompt"]) # Header row
    
    for combo in final_prompts:
        # Join the combination elements into a single readable string
        prompt_string = f"{combo[0]} based on the {combo[1]} {combo[2]}. {combo[3]}, {combo[4]}."
        writer.writerow([prompt_string])

print(f"Success! {len(final_prompts)} highly unique prompts have been saved to {filename}.")
# 