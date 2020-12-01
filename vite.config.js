// vite.config.js
export default {
  proxy: {
    // string shorthand
    //'/foo': 'http://localhost:4567/foo',
    // with options
    '/api': {
      target: 'http://127.0.0.1:8000/api/',
      changeOrigin: true,
      rewrite: path => path.replace(/^\/api/, '')
    }
  }
}
