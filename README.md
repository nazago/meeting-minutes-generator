# MEETING MINUTES GENERATOR

During a meeting or a lecture, you are focus on what it is being said, not on taking notes. Let an LLM do this for you!
You just need a computer (a laptop without GPU is totally fine). Take the .wav file through your computer or phone, and then feed it to the program which you can run locally on your machine, so you have full privacy over your data.

## PARAMETERS

In config.py you can set:

- AUDIO_FILEPATH (str): The relative path to the audio file that will be processed.
- LLM_MODEL (str): The language model to be used for analyzing or generating text based on the input.
- BACKGROUND_INFO (str): Relevant background information that provides context for the task. As an example,
it describes the company's financial struggles in the last quarter, including near-bankruptcy.

## Features

- Run for free, offline and total privacy your LLM on audio of your meetings or lectures (with the consent of everyone, of course).
- Choose the LLM to summarize and make the action points.

## Quickstart

A virtual environment is preferred, but optional.

1. First of all, install the package required to run the application:

```shell
pip install -r requirements.txt
```

2. Then, make sure to have [Ollama](https://ollama.com/) installed (it is literally one line of code in the terminal).
3. Make the local server on your machine to run the neural networks:

```shell
ollama serve &
```

The neural network I suggest to install (using `ollama pull <model>`) is Qwen7B.

1. You are ready to run the program and query your documentation! Run the program:

```shell
python main.py
```

You should see something like:

```shell
$ python main_rag.py 
Loading Whisper ASR model...
Transcribing audio...
Transcript:
Good afternoon everyone and welcome to FinTech Plus SYNC's second quarter 2023 earnings call. I'm John Doe, CEO of FinTech Plus.
We've had a stellar Q2 with a revenue of 125 million. A 25% increase year over year. Our gross profit margin stands at a solid 58% due in part to cost efficiencies gaining our scalable business model.
Our EBITDA has surged to $37.5 million, translating to a remarkable 30% EBITDA margin. Our net income for the quarter rose to 16 million which is a note worthy increase from 10 million in Q2 2022.
Our total addressable market has grown substantially thanks to the expansion of our high yield savings product line in the new Robo Advisor platform. 
We've been diversifying our asset-back securities portfolio investing heavily in collateralized debt obligations and residential mortgage-back securities. 
We've also invested 25 million in AAA rated corporate bonds enhancing our risk-adjusted returns. As for a balance sheet, total assets reached 1.5 billion with total liabilities at 900 million, leaving us with a solid equity base of 600 million.
Our debt-to-equity ratio stands at 1.5, a healthy figure considering our expansionary phase. We continue to see substantial organic user growth with customer acquisition cost dropping by 15% and lifetime value growing by 25%.
Our LTV-CAC ratio is at an impressive 3.5% X. In terms of risk management, we have a value at risk model in place with a 99% confidence level indicating that our maximum loss will not exceed 5 million in the next trading day.
We've adopted a conservative approach to managing our leverage and have a healthy tier-run capital ratio of 12.5%. Our forecast for the coming quarter is positive.
We expect revenue to be around 135 million and a percent quarter over quarter growth driven primarily by our cutting-edge blockchain chain solutions and AI driven predictive analytics.
We're also excited about the upcoming IPO of our FinTech subsidiary Pay Plus which we expect to raise 200 million. Significantly bolstering our liquidity and paving the way for aggressive growth strategies.
We thank our shareholders for their continued faith in us and we look forward to an even more successful Q3. Thank you so much.
Elaborating the transcript..
AI BOT reply:
 Here's a summary of the transcript with extracted action points:

**Summary:**

FinTech Plus SYNC's CEO, John Doe, reported strong second-quarter 2023 earnings, driven by revenue growth, cost efficiencies, and strategic investments. The company has made significant progress since its poor Q1 performance, which brought them close to bankruptcy.

**Action Points:**

1. **Revenue Growth:** Revenue increased by 25% year-over-year to $125 million in Q2 2023.
2. **Cost Efficiencies:** Gross profit margin improved to 58%, driven by cost efficiencies and a scalable business model.
3. **EBITDA Margin:** EBITDA surged to $37.5 million, translating to a remarkable 30% EBITDA margin.
4. **Net Income:** Net income rose to $16 million, a notable increase from Q2 2022.
5. **Total Addressable Market (TAM):** TAM grew substantially due to the expansion of high-yield savings products and the Robo Advisor platform.
6. **Asset-Back Securities Portfolio:** The company diversified its portfolio by investing in collateralized debt obligations, residential mortgage-backed securities, and AAA-rated corporate bonds.
7. **Balance Sheet:**
        * Total assets reached $1.5 billion.
        * Total liabilities stood at $900 million, leaving a solid equity base of $600 million.
        * Debt-to-equity ratio was 1.5, considered healthy for an expansionary phase.
8. **Risk Management:** The company implemented a value-at-risk model with a 99% confidence level, indicating that maximum loss would not exceed $5 million in the next trading day.
9. **Leverage and Capital Ratio:** The company adopted a conservative approach to managing leverage and maintained a healthy tier-1 capital ratio of 12.5%.
10. **Forecast:**
        * Revenue is expected to be around $135 million in Q3, driven by cutting-edge blockchain chain solutions and AI-driven predictive analytics.
        * The upcoming IPO of FinTech subsidiary Pay Plus is expected to raise $200 million, significantly bolstering liquidity and paving the way for aggressive growth strategies.

Overall, the company has made significant progress since its poor Q1 performance, and the CEO remains optimistic about future growth.
```

## Final remarks

Please feel free to contact me for any queries/collaborations!

## Next steps

- Speaker Diarization
- feel free to propose!
