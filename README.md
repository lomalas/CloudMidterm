Type C: This would be a custom project keeping track of its own snapshots

The project will be a simplified market simulator. There are many stretch goals I might possilbly go for 
but I think for now it will have a group of comapnies (lets say 10) and the simulation will keep track of 
and display movements in stock price. The generation will start semi random and possibly become based on 
agentic predictions. 

I may also include currencies, countries, bonds, media, stock portfilios and expansive UI, but for now
these are stretch goals. 

Final version:
This project ended up changing a lot form the original vision, mostly just based on time constraints. Because of this there are a lot of files that are included that are unnessacery for the final version. If you want the relevant files for the jetstream2 version they are main.py, simulation/charts.py, simulation/controller.py, simulation/market_tick.py and simulation/snapshot.py. The other files should mostly be for the streamlit version, test files or setup. Below are some of the commands that you may find useful for exploring the project in no particular order

Run test simulation: python -m unittest simulation.test_simulation 

This is the original version of the project before Jetstream. It is not web hosted.
Run Test streamlit: 
venv\Scripts\activate
streamlit run visualization\steamlitGraphing.py

jetstream public link:
https://eco.149.165.159.157.nip.io/

Run local Version:
uvicorn main:app --host 127.0.0.1 --port 8000 --reload                                        


py -3.10 -m venv venv

.\venv\Scripts\Activate.ps1

get into virtual env: ssh -i ~/.ssh/jetstream2 exouser@149.165.159.157