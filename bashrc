# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(lesspipe)"
# some more ls aliases
alias lt='ls -ltr'
alias ll='ls -l'
alias la='ls -A'
alias cx="chmod a+x"
alias cr="chmod a+r"
#alias sa="sshmail ahorvath"
alias l='ls -CF'
alias ipythonlab='ipython -pylab'
alias pylab='ipython -pylab'
alias bzrstatushead='bzr status|head -23'
alias bzrlastrevisions='bzr log -r -5..'
alias ducks='su -cks * | sort -rn|head -11'
alias ..='cd ..'
alias ...='cd ~/cxnet/mfng'
alias aw='antiword   -m 8859-2.txt'
alias old="cd $OLDPWD"

#export PYTHONSTARTUP=.pythonrc.py
#export CDPATH=.:~
export LESSEDIT="%E ?lt+%lt. %f"
export EDITOR="vim"
#export VISUAL="gvim"
#alias ssh2="luit -encoding iso-8859-2 -- ssh"
#alias ssh4522="ssh -p 4522"
alias ns="luit -encoding iso-8859-2 -- ssh -p 4522 $NS"
alias sshdiak1="ssh -p 4522 diak1@mail.roik.bmf.hu"

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

#fortune de hu|cowthink
