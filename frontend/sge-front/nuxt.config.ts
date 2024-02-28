// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  typescript: {
    typeCheck: true
  },
  modules: [
    'nuxt-primevue'
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
  ]
})
