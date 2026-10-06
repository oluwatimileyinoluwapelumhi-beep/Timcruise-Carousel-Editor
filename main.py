#!/usr/bin/env python3
"""Simple runner for the Timcruise Carousel Editor."""

import argparse
from batch_carousel_editor import BatchCarouselEditor


def main():
    parser = argparse.ArgumentParser(description="Edit motivational posts and Storipod promos.")
    parser.add_argument("--mode", choices=["motivational", "storipod"], default="motivational",
                        help="Type of content to create")
    parser.add_argument("--input-dir", default="input_images",
                        help="Folder containing images to edit")
    parser.add_argument("--output-prefix", default="",
                        help="Optional prefix to add to output file names")
    parser.add_argument("--group-name", default="THE GROWTH NEXUS [INSIGHT & OUTLOOK]",
                        help="Your group name")
    parser.add_argument("--creator-name", default="@Timilocruise",
                        help="Your personal or creator name")
    args = parser.parse_args()

    editor = BatchCarouselEditor(group_name=args.group_name, creator_name=args.creator_name)

    if args.mode == "motivational":
        editor.batch_edit_motivational(args.input_dir, args.output_prefix)
    else:
        editor.batch_edit_storipod(args.input_dir, args.output_prefix)

    print("\nDone.")
    print("Your edited files are in the output folder for the selected mode.")


if __name__ == "__main__":
    main()
