## ITS with MFF-STGCN method.
This project's data is Shanghai parking flow.csv

It is raw data of Shanghai parking lots.

If you don't have it, please contact me.
## Code structure
  ├── README.md
  ├── __pycache__
  ├── _trial_temp
  │   ├── _trial_marker
  │   └── test.log
  ├── code
  │   ├── data_processing.py
  │   ├── model_training.py
  │   ├── utils.py
  │   ├── __pycache__
  │   ├── config_loader.py
  │   ├── data_visualization.py
  │   └── evaluation_metrics.py
  ├── data
  │   ├── raw_data
  │   │   ├── graph_signal_matrix.npz
  │   │   └── adjacency_matrix.csv
  │   ├── processed_data
  │   │   ├── train_data.npz
  │   │   ├── val_data.npz
  │   │   └── test_data.npz
  │   └── predictions
  │       ├── train_predictions.npy
  │       ├── val_predictions.npy
  │       └── test_predictions.npy
  ├── models
  │   ├── MFF-STGCN.py
  │   ├── astgcn.py
  │   ├── lstm.py
  │   ├── __pycache__
  │   ├── arima.py
  │   ├── gbm.py
  │   └── output
  │       ├── model_checkpoints
  │       └── trained_models
  ├── results
  │   ├── figures
  │   │   ├── training_loss.png
  │   │   ├── validation_accuracy.png
  │   │   └── test_predictions_vs_actual.png
  │   └── logs
  │       ├── training_log.txt
  │       ├── validation_log.txt
  │       └── test_log.txt
  └── requirements.txt
<!--
**AutumnwaterFlipped/AutumnwaterFlipped** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->
