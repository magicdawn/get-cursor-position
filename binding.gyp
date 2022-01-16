{
  "targets": [
    {
      "target_name": "pos",
      "sources": [ "src/pos.cc" ],
      "cflags_cc": ["-fPIC"],
      "include_dirs": [
        "<!(node -e \"require('nan')\")>"
      ]
    }
  ]
}
