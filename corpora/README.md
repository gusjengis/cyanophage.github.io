# Programming Corpus

This folder contains source material and a generator for a programming-heavy analysis corpus.

What it does:

- starts with the full existing `words-english.json` corpus as the prose base
- adds a large blended code corpus on top of that
- writes the result as `words-programming.json`

The default generator intentionally biases toward code:

- base English corpus: `1.0x`
- code overlay: `2.0x` the total mass of the full English corpus

That means the generated corpus is intentionally programming-heavy rather than balanced prose.

Generate it with:

```bash
python3 corpora/generate_words.py
```

You can tune the code bias with:

```bash
python3 corpora/generate_words.py --code-multiplier 3.0
```

Notes:

- code tokens are split on whitespace and lowercased to match the existing analyzer pipeline
- the old `prose/` folder is kept as downloaded source material from the earlier experiment, but the current programming corpus generator does not use it

Current code sources:

- original set
  - `requests_sessions.py` - Requests - https://raw.githubusercontent.com/psf/requests/main/src/requests/sessions.py
  - `node_fs.js` - Node.js - https://raw.githubusercontent.com/nodejs/node/v22.x/lib/fs.js
  - `typescript_core.ts` - TypeScript - https://raw.githubusercontent.com/microsoft/TypeScript/main/src/compiler/core.ts
  - `ripgrep_main.rs` - ripgrep - https://raw.githubusercontent.com/BurntSushi/ripgrep/master/crates/core/main.rs
  - `go_fmt_print.go` - Go - https://raw.githubusercontent.com/golang/go/master/src/fmt/print.go
  - `redis_server.c` - Redis - https://raw.githubusercontent.com/redis/redis/unstable/src/server.c
- expanded set
  - `cpython_argparse.py` - CPython - https://raw.githubusercontent.com/python/cpython/main/Lib/argparse.py
  - `django_models_base.py` - Django - https://raw.githubusercontent.com/django/django/main/django/db/models/base.py
  - `react_hooks.js` - React - https://raw.githubusercontent.com/facebook/react/main/packages/react/src/ReactHooks.js
  - `next_config.ts` - Next.js - https://raw.githubusercontent.com/vercel/next.js/canary/packages/next/src/server/config.ts
  - `vim_main.c` - Vim - https://raw.githubusercontent.com/vim/vim/master/src/main.c
  - `linux_sched_core.c` - Linux kernel - https://raw.githubusercontent.com/torvalds/linux/master/kernel/sched/core.c
  - `clang_format.cpp` - clang - https://raw.githubusercontent.com/llvm/llvm-project/main/clang/lib/Format/Format.cpp
  - `jdk_string.java` - OpenJDK - https://raw.githubusercontent.com/openjdk/jdk/master/src/java.base/share/classes/java/lang/String.java
  - `dotnet_string.cs` - .NET runtime - https://raw.githubusercontent.com/dotnet/runtime/main/src/libraries/System.Private.CoreLib/src/System/String.cs
  - `ruby_string.c` - Ruby - https://raw.githubusercontent.com/ruby/ruby/master/string.c
  - `rails_inflector_methods.rb` - Rails - https://raw.githubusercontent.com/rails/rails/main/activesupport/lib/active_support/inflector/methods.rb
  - `rustc_parser_mod.rs` - Rust compiler - https://raw.githubusercontent.com/rust-lang/rust/master/compiler/rustc_parse/src/parser/mod.rs
  - `godot_node.cpp` - Godot - https://raw.githubusercontent.com/godotengine/godot/master/scene/main/node.cpp
  - `tensorflow_training.py` - TensorFlow - https://raw.githubusercontent.com/tensorflow/tensorflow/master/tensorflow/python/keras/engine/training.py
