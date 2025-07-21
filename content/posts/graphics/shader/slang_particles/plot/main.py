import polars as pl
import matplotlib.pyplot as plt


def main():
    df = pl.read_csv("result.csv")
    print(df)

    df_greedy = df.filter(pl.col("type") == "greedy")
    df_tiled_256 = df.filter(pl.col("type") == "tiled_256")

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(df_greedy["num"], df_greedy["fps"], label="greedy")
    ax.plot(df_tiled_256["num"], df_tiled_256["fps"], label="tiled")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Number of Particles")
    ax.set_ylabel("FPS")
    ax.legend()
    ax.grid(True)
    plt.savefig("output/fps.png", dpi=300, bbox_inches="tight")


if __name__ == "__main__":
    main()
