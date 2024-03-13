// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  typescript: {
    typeCheck: true
  },
  modules: [
    'nuxt-primevue',
    '@sidebase/nuxt-auth'
  ],
  primevue: {
    components: {
      include: ['Button']
    }
  },
  css: [
    'primeicons/primeicons.css', //css dos ícones do primevue
    'primevue/resources/themes/aura-light-green/theme.css', // css tema dos componentes primevue
    '~/assets/style/global-variables.scss',  //variáveis css global customizado para toda a aplicação
    '~/assets/style/global-project.scss',  //css global customizado para toda a aplicação
  ],
  auth:{// estamos fazendo a configuração da biblioteca sidebase
    baseURL: 'http://localhost:8000',// endereço do backend
    provider: {
      type: 'local', //biblioteca sidebase no modo local (webToken)
      endpoints: {
        signIn: { path: '/token/login', method: 'post'}, //endereço do joser, comunicando duas bibliotecas, para conseguir fazer login 
        signOut: { path: '/token/logout', method: 'post'},        
        getSession: { path: '/users', method: 'get'}, //endereço para configurar token
      },
      token: {signInResponseTokenPointer: '/auth_token', type: 'Token'},
      pages: {login:'/'} //endereço da pagina de login do
    }
  }
})
