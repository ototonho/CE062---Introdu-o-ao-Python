# pelo terminal
# git config --global user.name 'seu nome'
# git config --global user.email 'seu@email.com'

# pelo pacote usethis
library(usethis)
use_git_config(user.name = "user name",
               user.email = "pipipi@email.com")

# para gerar o token 
usethis::create_github_token()

gitcreds::gitcreds_set()

