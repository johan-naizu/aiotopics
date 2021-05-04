![aiotopics](https://i.imgur.com/1248yt1.png)

# aiotopics
Fetch random topics to start conversations.
Ideal for discord and other social media bots.

![Downloads](https://pepy.tech/badge/aiotopics) ![PyPI](https://img.shields.io/pypi/v/aiotopics) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aiotopics) ![PyPI - License](https://img.shields.io/pypi/l/aiotopics)
## Installation
```pip
pip install aiotopics
```
## Usage
```python
import aiotopics
topic=await aiotopics.get_topic()
print(topic)