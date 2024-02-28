<script setup lang="ts">
    import { ref, computed } from 'vue'

    /*
    exemplos para explicar typescript
    const teste = 'ok'
    const value1 = ref(0)
    const value2 = ref(0)   
    const makeMul = (n1:number,n2:number):number => n1 * n2

    const result = computed(()=> makeMul(value1.value,value2.value))*/
</script>

<template>
    <!--
    <div>
        <h1>My HomePage!!!</h1>
        <p>{{ teste }}</p>
        <input type="text" v-model="value1">
        <input type="text" v-model="value2">
        <p>Result: {{ result }}</p>
    </div>-->
    <main class="login_main"> 
        <!-- content of logo image -->
        <section class="logo_panel">
            <img src="/sge.jpeg" alt="sge logo">
            <h1>Sistema de Gestão de Ensino</h1>
            <p>&reg; Senai Roberto Mange</p>
            <div class="stars1"></div>
            <div class="stars2"></div>
            <div class="stars3"></div>
        </section>

         <!-- content of login form -->
         <section class="login_panel">
            <h1>teste</h1>
        </section>
    </main>
</template>

<style scoped lang="scss">

    .login_main{
        width: 100vw;
        height: 100vh;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;
        background-color: var(--dark-background-color);

        .logo_panel{
            display: none;
        }

        .login_panel{
            width: 100vw;
            height: 100vh;  
            background-color: var(--light-background-color);
        }
    }

    @media screen and (min-width: 550px){
        .login_main{
            .logo_panel{
                display: flex;
            }
        }
    }

        

</style>