{
  description = "Python shell for AtCoder";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";

    mach-nix.url = "mach-nix/3.5.0";
  };

  outputs = { self, nixpkgs, mach-nix, ... }:
    let
      pythonVersion = "python311";
      system = "aarch64-darwin";

      pkgs = nixpkgs.legacyPackages.${system};

      mach = mach-nix.lib.${system};
      pythonEnv = mach.mkPython {
        python = pythonVersion;
        requirements = builtins.readFile ./requirements.txt;
      };
    in
    {

      devShells.${system}.default = pkgs.mkShell {
        packages = with pkgs; [
          pythonEnv
          nodePackages.pyright
        ];

        shellHook = ''
          export PYTHONPATH="${pythonEnv}/bin/python"
        '';
      };
    };
}
