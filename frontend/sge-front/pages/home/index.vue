<script setup lang="ts"> 
const {signOut} = useAuth();

definePageMeta({
    middleware: 'auth'
})

const submitLogout = ()=>{
    
    signOut({redirect: false}).then(()=>{
                console.log("Volto a página inicial!");
                navigateTo('/');
            })

            .catch((error)=>{
            console.log("Error when trying to login: ", error);
        });
    }



</script>


<template>
    <div>
        <h1>minha tela home</h1>
        <button @click="submitLogout" class="customButton">SAIR</button>
    </div>
</template>

<style lang="scss">

</style>
