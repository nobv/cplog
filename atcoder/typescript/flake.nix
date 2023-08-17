{
  description = "TypeScript shell for AtCoder";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs, ... }:
    let
      system = "aarch64-darwin";
      pkgs = nixpkgs.legacyPackages.${system};
    in
    {

      devShells.${system}.default = pkgs.mkShell {
        packages = with pkgs; [
          nodejs_18
          typescript
          nodePackages.prettier
          nodePackages.typescript-language-server
        ];
      };
    };
}

