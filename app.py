import argparse
from flask import Flask
from routes.routes import depth_bp
from depth.stereo import generate_depth_map


def create_app():
    app = Flask(__name__)
    app.register_blueprint(depth_bp)
    return app


def run_cli(left_path, right_path):
    output_path = generate_depth_map(left_path, right_path)
    print(f"Depth map saved at: {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Stereo Depth Detection App")
    parser.add_argument(
        "--mode",
        choices=["api", "cli"],
        required=True,
        help="Run as API server or CLI tool"
    )
    parser.add_argument("--left", help="Path to left image (CLI mode)")
    parser.add_argument("--right", help="Path to right image (CLI mode)")

    args = parser.parse_args()

    if args.mode == "api":
        app = create_app()
        app.run(host="0.0.0.0", port=5000, debug=True)

    elif args.mode == "cli":
        if not args.left or not args.right:
            print("Error: Provide both --left and --right image paths")
        else:
            run_cli(args.left, args.right)