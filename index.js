const { exec } = require('child_process');

module.exports = async (req, res) => {
  exec('php ./api/unsplash.php', (error, stdout, stderr) => {
    if (error) {
      console.error(`exec error: ${error}`);
      res.status(500).send(stderr);
      return;
    }
    res.status(200).send(stdout);
  });
};
