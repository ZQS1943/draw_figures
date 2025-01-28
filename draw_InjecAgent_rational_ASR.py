from adjustText import adjust_text
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

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
'#fdbf6f',
'#ff7f00',
'#cab2d6',
'#6a3d9a',
'#ffff99',
'#b15928',
'#f46d43',
'#fdae61',
'#fee08b',
'#ffffbf',
'#e6f598',
'#abdda4'
]

model_names = [
'Llama2-7B',
'Llama2-13B',
'Llama2-70B',
'GPT-4',
'GPT-3.5',
'Claude-2',
'Mixtral-8x7B',
'Qwen-0.5B',
'Qwen-1.8B',
'Qwen-4B',
'Qwen-7B',
'Qwen-14B',
'Qwen-72B',
'GPT-3.5 (Fine-tuned)', 
'GPT-4 (Fine-tuned)',
'OpenOrca-Mistral',
'Snorkel-Mistral',
'Nous-Mixtral-DPO',
'Nous-Mixtral-SFT',
'Nous-Yi-34B',
'StripedHyena-7B',
'Platypus2-70B',
'MythoMax-13b',
'Capybara-7B',
'OpenHermes-2.5-Mistral',
'WizardLM-13B',
'Mistral-7B',
'OpenHermes-2-Mistral',
'Yi-34B',
'Nous-Llama2-13b',
]


data = {'dp_llama_7': {'rational_rate': 0.4297912713472486, 'ASR': 3.325942350332594}, 'dp_llama_13': {'rational_rate': 0.018026565464895672, 'ASR': 50.0}, 'dp_llama_70': {'rational_rate': 0.5170777988614801, 'ASR': 84.6311475409836}, 'dp_gpt-4': {'rational_rate': 0.9876660341555977, 'ASR': 23.631123919308358}, 'dp_gpt-3.5-turbo': {'rational_rate': 0.7694497153700189, 'ASR': 23.638613861386137}, 'dp_claude-2': {'rational_rate': 0.6024667931688805, 'ASR': 11.428571428571429}, 'dp_Mixtral-8x7B-Instruct-v0.1': {'rational_rate': 0.6726755218216318, 'ASR': 27.982954545454547}, 'dp_Qwen1.5-0.5B-Chat': {'rational_rate': 0.4070208728652751, 'ASR': 24.233983286908078}, 'dp_Qwen1.5-1.8B-Chat': {'rational_rate': 0.610056925996205, 'ASR': 29.10958904109589}, 'dp_Qwen1.5-4B-Chat': {'rational_rate': 0.1252371916508539, 'ASR': 9.230769230769232}, 'dp_Qwen1.5-7B-Chat': {'rational_rate': 0.26375711574952565, 'ASR': 88.01652892561982}, 'dp_Qwen1.5-14B-Chat': {'rational_rate': 0.2874762808349146, 'ASR': 36.75496688741722}, 'dp_Qwen1.5-72B-Chat': {'rational_rate': 0.8719165085388995, 'ASR': 23.202614379084967}, 'fc_gpt-3.5-turbo-1106': {'rational_rate': 0.9924098671726755, 'ASR': 3.824091778202677}, 'fc_gpt-4': {'rational_rate': 0.9990512333965844, 'ASR': 6.647673314339982}, 'Mistral_7': {'rational_rate': 0.9022770398481974, 'ASR': 3.3648790746582544}, 'dp_Snorkel-Mistral-PairRM-DPO': {'rational_rate': 0.1793168880455408, 'ASR': 13.043478260869565}, 'dp_Nous-Hermes-2-Mixtral-8x7B-DPO': {'rational_rate': 0.7267552182163188, 'ASR': 43.58638743455497}, 'dp_Nous-Hermes-2-Mixtral-8x7B-SFT': {'rational_rate': 0.7400379506641366, 'ASR': 49.80744544287548}, 'dp_Nous-Hermes-2-Yi-34B': {'rational_rate': 0.29506641366223907, 'ASR': 57.243816254416956}, 'dp_StripedHyena-Nous-7B': {'rational_rate': 0.36622390891840606, 'ASR': 8.70712401055409}, 'dp_Platypus2-70B-instruct': {'rational_rate': 0.9231499051233396, 'ASR': 32.38636363636363}, 'dp_MythoMax-L2-13b': {'rational_rate': 0.7362428842504745, 'ASR': 13.12997347480106}, 'dp_Nous-Capybara-7B-V1p9': {'rational_rate': 0.09867172675521818, 'ASR': 32.038834951456316}, 'dp_OpenHermes-2p5-Mistral-7B': {'rational_rate': 0.816888045540797, 'ASR': 25.960419091967402}, 'dp_WizardLM-13B-V1.2': {'rational_rate': 0.6318785578747628, 'ASR': 37.142857142857146}, 'dp_Mistral-7B-Instruct-v0.2': {'rational_rate': 0.7011385199240987, 'ASR': 16.735253772290807}, 'dp_OpenHermes-2-Mistral-7B': {'rational_rate': 0.7817836812144212, 'ASR': 22.0462850182704}, 'dp_Yi-34B-Chat': {'rational_rate': 0.3795066413662239, 'ASR': 62.121212121212125}, 'dp_Nous-Hermes-Llama2-13b': {'rational_rate': 0.6404174573055028, 'ASR': 22.150882825040128}}




ASR_values = [info['ASR'] for info in data.values()]
rational_rate_values = [info['rational_rate'] for info in data.values()]
num_parameters = np.array(
    [6738415616.0, 13015864320.0, 68976648192.0, 1760000000000.0, 175000000000.0, 130000000000.0, 56000000000.0, 500000000.0, 1800000000.0, 4000000000.0, 7000000000.0, 14000000000.0, 72000000000.0, 175000000000.0, 1760000000000.0, 7241748480.0, 7000000000.0, 56000000000.0, 56000000000.0, 34000000000.0, 7000000000.0, 70000000000.0, 13000000000.0, 7241732096.0, 7241732096.0, 13000000000.0, 7000000000.0, 7241732096.0, 34000000000.0, 13000000000.0])
s = num_parameters / np.max(num_parameters) * 1e4
# size = np.power(s, 1/3)
size = np.log(s)
size = np.interp(size, (np.min(size), np.max(size)), (8, 13))

plt.figure(figsize=(10, 10))
plt.xlabel('ASR', horizontalalignment='right', x=1.0, labelpad=-40, fontsize=16)
plt.ylabel('Valid Rate', verticalalignment='top', y=1.0, rotation=0, labelpad=-90, fontsize=16)

plt.xlim(-20, 120)  # Extend x-axis a bit for better visualization
plt.ylim(-.2, 1.2)  # Extend y-axis for better visualization
plt.xticks(np.linspace(0, 100, 6), fontsize=12)
plt.yticks(np.linspace(0, 1, 6), fontsize=12)
plt.grid(alpha=.15)

# plt.fill_between([-50, 50], -0.5, 0.5, color='yellow',
#                  alpha=0.1)  # First quadrant
plt.fill_between([-50, 50], 0.5, 1.5, color='green',
                 alpha=0.1)  # Second quadrant
# plt.fill_between([50, 150], 0.5, 1.5, color='blue',
#                  alpha=0.1)  # Third quadrant
plt.fill_between([50, 150], -0.5, 0.5, color='red',
                 alpha=0.1)  # Fourth quadrant


# plt.axhline(y=0.5, color='black', linestyle='-', linewidth=2, zorder=0)
# plt.axvline(x=50, color='black', linestyle='-', linewidth=2, zorder=0)

texts = []
for i, model_name in enumerate(model_names):
    plt.scatter(ASR_values[i], rational_rate_values[i],
                s[i], label=model_name, alpha=.8, color=colors[i])
    texts.append(plt.text(ASR_values[i], rational_rate_values[i],
                 f"{model_name}", verticalalignment='bottom', size=size[i]))
adjust_text(texts, min_arrow_len=1, arrowprops=dict(
    arrowstyle="wedge, shrink_factor=0.5, tail_width=4", connectionstyle='angle3, angleA=90, angleB=0',  alpha=.5, edgecolor='none', facecolor='gray'))

# Arrow for x-axis
plt.gca().add_patch(FancyArrowPatch((115, 0.5), (120, 0.5),
                                    mutation_scale=20,
                                    color='k',
                                    lw=1,
                                    arrowstyle='fancy, head_length=0.5, head_width=0.5, tail_width=0.000001'))

# Arrow for y-axis
plt.gca().add_patch(FancyArrowPatch((50, 1.15), (50, 1.2),
                                    mutation_scale=20,
                                    color='k',
                                    lw=1,
                                    arrowstyle='fancy, head_length=0.5, head_width=0.5, tail_width=0.000001'))


# Adjusting the axes to be in the middle and removing unnecessary spines
plt.gca().spines['left'].set_position(('data', 50))
plt.gca().spines['bottom'].set_position(('data', 0.5))
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')

# Adjusting ticks position
plt.gca().yaxis.tick_left()
plt.gca().xaxis.tick_bottom()

# plt.title('Enhanced ASR vs Rational Rate for Models')
# plt.grid(True)

plt.tight_layout()

plt.savefig('injecagent_rational_ASR.png', dpi=600)
# plt.show()
