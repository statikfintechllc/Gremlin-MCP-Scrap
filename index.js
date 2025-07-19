#!/usr/bin/env node

/**
 * GremlinGPT MCP Scraper Launcher
 * 
 * Boots the Flask MCP service with a clean, reliable startup
 * - Installs pinned Python requirements
 * - Launches the crawler server
 */

const { spawn } = require('child_process');
const path = require('path');
const chalk = require('chalk');

console.log(chalk.cyanBright('[MCP] Booting Gremlin Scraper MCP...'));

const BASE_DIR    = __dirname;
const REQ_FILE    = path.join(BASE_DIR, 'requirements.txt');
const SERVER_PY   = path.join(BASE_DIR, 'server.py');

function installDependencies() {
  return new Promise((resolve, reject) => {
    console.log(chalk.green('[MCP] Installing Python dependencies...'));
    const pip = spawn('pip3', ['install', '-r', REQ_FILE], {
      stdio: 'inherit',
      shell: true
    });

    pip.on('exit', (code) => {
      if (code === 0) {
        console.log(chalk.green('[MCP] Python dependencies installed.'));
        resolve();
      } else {
        reject(new Error(`pip install failed with exit code ${code}`));
      }
    });

    pip.on('error', (err) => {
      reject(new Error(`pip execution failed: ${err.message}`));
    });
  });
}

function launchServer() {
  console.log(chalk.green('[MCP] Launching Flask server...'));
  const server = spawn('python3', [SERVER_PY], {
    stdio: 'inherit',
    shell: true
  });

  server.on('exit', (code) => {
    if (code === 0) {
      console.log(chalk.greenBright('[MCP] Server shut down cleanly.'));
    } else {
      console.warn(chalk.yellow(`[MCP] Server exited with code ${code}`));
    }
    process.exit(code);
  });

  server.on('error', (err) => {
    console.error(chalk.red(`[MCP] Failed to start server: ${err.message}`));
    process.exit(1);
  });
}

(async () => {
  try {
    await installDependencies();
    launchServer();
  } catch (err) {
    console.error(chalk.red(`[MCP] Setup error: ${err.message}`));
    process.exit(1);
  }
})();
