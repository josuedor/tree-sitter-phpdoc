{
  "targets": [
    {
      "target_name": "tree_sitter_phpdoc_binding",
      "include_dirs": [
        "<!(node -e \"require('nan')\")",
        "src"
      ],
      "sources": [
        "src/parser.c",
        "src/binding.cc",
        "src/scanner.c"
      ],
      "cflags_c": [
        "-std=c99",
      ]
    }
  ]
}
