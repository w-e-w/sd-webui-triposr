import launch

if not launch.is_installed("torchmcubes"):
    launch.run_pip("install git+https://github.com/tatsy/torchmcubes.git", "requirements for torchmcubes")

if not launch.is_installed("rembg"):
    launch.run_pip("install rembg", "requirements for rembg")
