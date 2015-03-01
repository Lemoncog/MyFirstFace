module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    watch: {
      scripts: {
        files: ['src/**/*.c'],
        tasks: ['exec:build', 'exec:install'],
        options: {
          spawn: false,
        },
      }
    },
    exec: {
      echo_something: 'echo "This is something"',
      build: 'pebble build',
      install: 'pebble install --emulator basalt'
    }
  });

  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-exec');

  // Default task(s).
  grunt.registerTask('default', ['watch', 'exec']);
};