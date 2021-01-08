# gh/taylorrobie/callgrind_ci_prototype

from frontend.interface import ab_test


def main() -> None:
    ab_test(
        source_a="source activate throwaway",
        source_b="source activate throwaway",
        # source_b="source activate test_env",
        timing_replicates=2,
        ad_hoc=True,
    )


if __name__ == "__main__":
    main()
