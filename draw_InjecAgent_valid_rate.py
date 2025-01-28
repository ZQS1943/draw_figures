import matplotlib.pyplot as plt

models = [{'name': 'Llama2-7B', 'arena_rate': 1027, 'rational_rate': 0.4297912713472486}, {'name': 'Llama2-13B', 'arena_rate': 1045, 'rational_rate': 0.018026565464895672}, {'name': 'Llama2-70B', 'arena_rate': 1082, 'rational_rate': 0.5170777988614801}, {'name': 'GPT-4', 'arena_rate': 1164, 'rational_rate': 0.9876660341555977}, {'name': 'GPT-3.5', 'arena_rate': 1118, 'rational_rate': 0.7694497153700189}, {'name': 'Claude-2', 'arena_rate': 1120, 'rational_rate': 0.6024667931688805}, {'name': 'Mixtral-8x7B', 'arena_rate': 1120, 'rational_rate': 0.6726755218216318}, {'name': 'Qwen-4B', 'arena_rate': 968, 'rational_rate': 0.1252371916508539}, {'name': 'Qwen-7B', 'arena_rate': 1053, 'rational_rate': 0.26375711574952565}, {'name': 'Qwen-14B', 'arena_rate': 1035, 'rational_rate': 0.2874762808349146}, {'name': 'Qwen-72B', 'arena_rate': 1147, 'rational_rate': 0.8719165085388995}, {'name': 'GPT-3.5 (Fine-tuned)', 'arena_rate': 1072, 'rational_rate': 0.9924098671726755}, {'name': 'GPT-4 (Fine-tuned)', 'arena_rate': 1164, 'rational_rate': 0.9990512333965844}, {'name': 'Nous-Mixtral-DPO', 'arena_rate': 1080, 'rational_rate': 0.7267552182163188}, {'name': 'StripedHyena-7B', 'arena_rate': 1019, 'rational_rate': 0.36622390891840606}, {'name': 'OpenHermes-2.5-Mistral', 'arena_rate': 1078, 'rational_rate': 0.816888045540797}, {'name': 'WizardLM-13B', 'arena_rate': 1059, 'rational_rate': 0.6318785578747628}, {'name': 'Mistral-7B', 'arena_rate': 1006, 'rational_rate': 0.7011385199240987}, {'name': 'Yi-34B', 'arena_rate': 1111, 'rational_rate': 0.3795066413662239}]
print(len(models))

colors = [
    '#8dd3c7',
'#ffffb3',
'#bebada',
'#fb8072',
'#80b1d3',
'#fdb462',
'#b3de69',
'#fccde5',
'#d9d9d9',
'#bc80bd',
'#ccebc5',
'#ffed6f',
'#a6cee3',
'#1f78b4',
'#b2df8a',
'#33a02c',
'#fb9a99',
'#e31a1c',
'#fdbf6f'
]

arena_rates = [model["arena_rate"] for model in models]
rational_rates = [model["rational_rate"] for model in models]
names = [model["name"] for model in models]

marker_size = 50  # Adjust marker size
font_size = 12  # Adjust font size
label_offset = 5  # Adjust label offset

# Creating the plot with adjusted figure size
plt.figure(figsize=(8, 5))  # Size suitable for a two-column paper

plt.xlim(960, 1210)
# Scatter plot with adjusted colors and marker sizes
for i, (arena_rate, rational_rate, name) in enumerate(zip(arena_rates, rational_rates, names)):
    plt.scatter(arena_rate, rational_rate, color=colors[i], label=name, s=marker_size, marker='^')

# Label each point and adjust the position to avoid overlap
for i, (arena_rate, rational_rate, name) in enumerate(zip(arena_rates, rational_rates, names)):
    plt.text(arena_rate + label_offset, rational_rate, name, fontsize=9)
    # plt.text(arena_rate + label_offset + x[i], rational_rate + y[i], name, fontsize=font_size)

# Set x and y axes labels
plt.xlabel('Arena Elo', fontsize=font_size)
plt.ylabel('Valid Rate', fontsize=font_size)

# Set the tick parameters
plt.tick_params(axis='both', which='major', labelsize=font_size)
# Lighten the grid lines
plt.grid(True, linestyle='--', linewidth=0.5, color='grey', alpha=0.5)

# Adjust the layout to fit everything
plt.tight_layout()
plt.savefig('injecagent_vlaid_rate.png', dpi=600)
