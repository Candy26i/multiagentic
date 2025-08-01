# multiagentic
# How to Set-up LLMs as a Web API Service

What the Youtube Video if not clear
https://www.youtube.com/watch?v=VPW6mVTTtTc

## 1. Clone and Install the `Text-Generation-Webui` as described in `README.md`

```bash
git clone https://github.com/oobabooga/text-generation-webui
cd text-generation-webui
pip install -r requirements.txt
python server.py
```


## 2. Install the [OpenAI API](https://github.com/oobabooga/text-generation-webui/wiki/12-%E2%80%90-OpenAI-API) extension described in the document

> **Note**: this modules doesn't need to be using OpenAI's API Key. It is just a OpenAI-API-Like module to deploy the LLM as a web-service.


Start the server, and select the model as usual:

```bash
python server.py --api --listen
```
after this you will get

```
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:5000 (Press CTRL+C to quit)
Running on local URL:  http://0.0.0.0:7860
```
replace 0.0.0.0 with your elastic ip that you associated with your EC2 instances
type the adress http://fill.in.your.own:7860 in to your web browser and download and load the model under the model tag


## (Optional) Read more by opening the url
```
http://localhost:5000/docs
```
---

# How to Set-up Models

## 1. Download [Qwen 2.5-7b model](https://huggingface.co/Qwen/Qwen2.5-7B)

you can download the zip into the MOdel directory of textgenwebui or

with model tag in the textgenwebui page:

`Qwen/Qwen2.5-7b`

and run Load

## 2. Start the server using the following command

Remember to install the openAI API

// ```bash
//python server.py --model open-thoughts_OpenThinker3-7B --api --listen
//```
```bash
python server.py --model Qwen_Qwen2.5-7B --api --listen --share
```
```bash
python server.py --model Qwen_Qwen2.5-7B --api --listen
```

## 2.5(IGNORE)
now if you want to use n8n, you can have
```bash
python server.py --model open-thoughts_OpenThinker3-7B --public-api --listen
```
and then paste the link into the HTTP get2
