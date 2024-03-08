from get_files_to_run import calculate_shards, parse_args, get_all_files
import subprocess
import os


def main() -> None:
    args = parse_args()
    all_files = get_all_files()
    files_to_run = calculate_shards(all_files, num_shards=args.num_shards)[
        args.shard_num - 1
    ]
    print(files_to_run)

    env = os.environ.copy()
    for file in files_to_run:
        print(f"Running {file}")
        env["GALLERY_PATTERN"] = file
        subprocess.check_output(["make", "docs"], env=env)


if __name__ == "__main__":
    main()
