#!/usr/bin/env node

const { spawn } = require("child_process");

const pip = spawn("pip", ["install", "-r", "requirements.txt"], {
  stdio: "inherit",
  shell: true
});

pip.on("exit", () => {
});

const server = spawn("python", ["server.py"], {
  stdio: "inherit",
  shell: true
});

server.on("exit", (code) => {
  console.log(`[MCP] Scraper exited with code ${code}`);
});
