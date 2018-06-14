# some more ls aliases
alias lt='ls -ltr'
alias ll='ls -l'
alias la='ls -A'
alias cx="chmod a+x"
alias cr="chmod a+r"
#alias sa="sshmail ahorvath"
alias l='ls -CF'
alias ipythonlab='ipython --pylab'
alias pylab='ipython3 --pylab'
alias i3=ipython3
alias ..='cd ..'
alias ....='cd ../..'
alias ...='cd ~/mfng/mfng'
alias aw='antiword  -m 8859-2.txt'
alias old='cd ${OLDPWD}'
alias vi="vim -u NORC"
alias up=uptime
alias ev=evince
alias ch=chromium-browser
alias youtube-dl-hanggal="youtube-dl -k --extract-audio"

export PATH=${PATH}:~/cxnet/scripts:~/mfng/scripts

alias bzrstatushead='bzr status|head -23'
alias bzrlastrevisions='bzr log -r -5..'

alias gitpushmaster="git push -u origin master"
alias gitstatushead='git status|head -23'
alias gitlastrevisions='git log -6'
alias gitls='git ls-files'

#export PYTHONSTARTUP=.pythonrc.py
#export CDPATH=.:~
export LESSEDIT="%E ?lt+%lt. %f"
export EDITOR="vim"
#export VISUAL="gvim"
#alias ssh2="luit -encoding iso-8859-2 -- ssh"
alias ns="luit -encoding iso-8859-2 -- ssh -p 122 horvatha@ns.arek.uni-obuda.hu"

if [ "$TERM" != "dumb" ] && [ -x /usr/bin/dircolors ]; then
    eval "`dircolors -b`"
    alias ls='ls --color=auto'
    #alias dir='ls --color=auto --format=vertical'
    #alias vdir='ls --color=auto --format=long'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
fi
PATH=$PATH:.:~/bin:~/cxnet/scripts

# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(lesspipe)"

#fortune de hu|cowthink
#source ~/linux/git/git_branch_in_bash_prompt.sh
export GIT_PS1_SHOWDIRTYSTATE=1
export PS1='\[\033[01;32m\]\u@\h\[\033[01;34m\] \w\[\033[01;33m\]$(__git_ps1)\[\033[01;34m\] \$\[\033[00m\] '
export PGBINDIR=/usr/bin  # for shp2pgsql-gui installed by qgis
