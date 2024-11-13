import argparse


def create_cli():
    parser = argparse.ArgumentParser(description="Telegram management assistant.")
    parser.add_argument(
        "--token", "-t", nargs="?", type=str, default=None, help="Telegram bot token."
    )
    parser.add_argument("--host-name", help="Set webhook host name.")
    parser.add_argument(
        "--webhook-path",
        default="/api/webhook",
        help="URL Path for webhook (default=/api/webhook)",
    )

    return parser


def parse_args(parser: argparse.ArgumentParser):
    args = parser.parse_args()
    return args
