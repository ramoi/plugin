"vim-plug 설치
"iwr -useb https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim |`
"    ni "$(@($env:XDG_DATA_HOME, $env:LOCALAPPDATA)[$null -eq $env:XDG_DATA_HOME])/nvim-data/site/autoload/plug.vim" -Force
call plug#begin('~/.vim/plugged')

Plug 'preservim/nerdtree'
Plug 'preservim/tagbar'
Plug 'Xuyuanp/nerdtree-git-plugin'
Plug 'vim-airline/vim-airline'
Plug 'frazrepo/vim-rainbow'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}
Plug 'mg979/vim-visual-multi', {'branch': 'master'}

call plug#end()

nmap <F9> :NERDTreeToggle
nmap <F8> :TagbarToggle


let g:VM_leader = ','

" .vimrc 설정 추가 
"Syntax Highligthing
if has ("syntax")
    syntax on
endif

set autoindent
set cindent      "C언어 자동 들여쓰기set nu

set smartindent
set tabstop=4
set expandtab
set shiftwidth=4

se nu
set incsearch
set hlsearch
