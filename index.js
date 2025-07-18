#!/usr/bin/env node

const { spawn } = require("child_process");
const path = require("path");
const chalk = require("chalk");

console.log(chalk.cyanBright("[MCP] Booting Gremlin Scraper MCP..."));

// Resolve full path in case of relative invocation
const reqPath = path.resolve(__dirname, "requirements.txt");
const serverPath = path.resolve(__dirname, "server.py");

// Step 1: Install dependencies
const pip = spawn("pip", ["install", "-r", reqPath], {
  stdio: "inherit",
  shell: true
});

pip.on("exit", (code) => {
  if (code !== 0) {
    console.error(chalk.red(`[MCP] Pip install failed with code ${code}`));
    process.exit(code);
  }

  console.log(chalk.green("[MCP] Python dependencies installed."));

  // Step 2: Launch the server
  const server = spawn("python", [serverPath], {
    stdio: "inherit",
    shell: true
  });

  server.on("exit", (serverCode) => {
    if (serverCode === 0) {
      console.log(chalk.greenBright(`[MCP] Server shut down cleanly.`));
    } else {
      console.warn(chalk.yellow(`[MCP] Server exited with code ${serverCode}`));
    }
    process.exit(serverCode);
  });

  server.on("error", (err) => {
    console.error(chalk.red(`[MCP] Failed to start server: ${err.message}`));
    process.exit(1);
  });
});

pip.on("error", (err) => {
  console.error(chalk.red(`[MCP] Pip execution failed: ${err.message}`));
  process.exit(1);
});
