# Llama-3.2-1B Infer Example

This is a demo that will show the exact same code (`llama_infer.py`) running either locally (if run with a PyTorch venv) or in the cloud (if run with a MyTorch venv).

## Output to Expect (mytorch)

```
python llama_infer.py      
You are already logged into Hugging Face, which makes me happy!!!
INFO - Client process is exiting; disconnecting from server...
INFO - Connecting to server proxy.mytorch.net:55553
*** Using GPU: Tesla P100-PCIE-16GB ***
Loading tokenizer for meta-llama/Llama-3.2-3B-Instruct...
INFO - Loading AutoTokenizer for `meta-llama/Llama-3.2-3B-Instruct`
INFO - ...AutoTokenizer has been loaded
Loading model for meta-llama/Llama-3.2-3B-Instruct...
INFO - Loading AutoModelForCausalLM model `meta-llama/Llama-3.2-3B-Instruct`
INFO - ...model has been loaded
Model loaded
Loading model onto cuda
Model moved to device
Tokenization complete

Generating response...

Prompt: Tell me a 500 word story about a black cat named George

Response:
]
George was a sleek and mysterious black cat with piercing green eyes that seemed to gleam in the dark. He had been a stray for as long as anyone could remember, but he never seemed to need anyone. He was a master of survival, able to scrounge up food and find shelter with ease.

Despite his tough exterior, George had a soft spot for humans. He would often sneak into homes and curl up in laps, purring contentedly as he basked in the warmth and attention. But he was a cat of discerning taste, and only sought out those who were willing to provide him with the finest treats and the most comfortable blankets.

One day, a young girl named Lily wandered into the neighborhood with her family. She was a shy and quiet child, with a mop of curly brown hair and a smile that could light up the darkest of rooms. As she explored the streets, she stumbled upon George lounging in a sunbeam, his eyes fixed intently on a nearby bird.

Lily gasped in wonder, her eyes locked onto George's piercing green gaze. For a moment, the two simply stared at each other, a connection sparking between them like a live wire. Then, to Lily's surprise, George stood up and began to pad towards her, his tail twitching with curiosity.

Lily hesitated for a moment, unsure of what to do. But something about George's gentle demeanor put her at ease, and she reached out a hand to pet him. George purred loudly, nuzzling her hand with his head, and Lily felt a sense of calm wash over her.

From that moment on, George and Lily were inseparable. They spent their days exploring the neighborhood, chasing after butterflies, and curled up together in the sunbeams that streamed through the windows. George taught Lily all about the art of napping, and how to find the perfect spot to watch the birds outside.

As the days turned into weeks, Lily's parents began to notice a change in their daughter. She seemed happier, more confident, and more at ease in her own skin. And whenever she looked into George's piercing green eyes, she felt a sense of peace and contentment wash over her.

One evening, as the sun set over the neighborhood, Lily snuggled up beside George on the couch. She stroked his soft fur, feeling the warmth of his body radiate into

Time taken: 25.64 seconds
INFO - Disconnecting from server...
INFO - Disconnected from server.
```

## Output to Expect (pytorch) on the Same Device (laptop)

```
python llama_infer.py 
You are already logged into Hugging Face, which makes me happy!!!
*** No GPU available ***
Loading tokenizer for meta-llama/Llama-3.2-3B-Instruct...
tokenizer_config.json: 100%|█████████████████████████████████████████████████| 54.5k/54.5k [00:00<00:00, 36.1MB/s]
tokenizer.json: 100%|████████████████████████████████████████████████████████| 9.09M/9.09M [00:01<00:00, 4.85MB/s]
special_tokens_map.json: 100%|████████████████████████████████████████████████| 296/296 [00:00<00:00, 916kB/s]
Loading model for meta-llama/Llama-3.2-3B-Instruct...
config.json: 100%|███████████████████████████████████████████████████████████| 878/878 [00:00<00:00, 2.46MB/s]
model.safetensors.index.json: 100%|██████████████████████████████████████████| 20.9k/20.9k [00:00<00:00, 14.4MB/s]
Downloading shards:   0%|                                                          | 0/2 [00:00<?, ?it/s]
```

> **Note:** Then go skiing for the day and comeback to read the adventures of George!