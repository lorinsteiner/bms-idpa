# Dependencies

| Dependency       | Description                                                                                                                               |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `torch`          | Deep learning framework for building and training the fully connected neural network, including automatic differentiation and optimizers. |
| `numpy`          | Library for numerical computing and matrix operations, used for data preprocessing and mathematical calculations.                         |
| `pandas`         | Data analysis library for loading the Fashion-MNIST CSV files and storing training metrics in tables.                                     |
| `matplotlib`     | Plotting library for creating and exporting figures such as learning curves.                                                              |
| `seaborn`        | Statistical visualization library built on Matplotlib, used for comparison plots across configurations and seeds.                         |
| `typer`          | Framework for building the command-line interface with subcommands such as `train`, `evaluate` and `plot`.                                |
| `rich`           | Terminal formatting library for progress bars and readable result tables in the console.                                                  |
| `pytest` _(dev)_ | Testing framework for checking that the network works correctly.                                                                          |
