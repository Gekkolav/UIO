#tar inn h, m og s.

  .globl	hms_to_sec
h,s_to_sec:
  movq	%rdi,%rax  # Hent flytter timer til rax.
  imulq $3600, %rax #Ganger timer med sekunder i rax
  imulq $60, %rsi #Ganger antall minutter med 60
  addq  %rsi, %rax #Legger til sekunder fra minutter
  addq  %rdx, %rax #Legger til sekunder

  ret


  .globl sec_to_h
sec_to_h:
  movq %RDI,%RAX
  movq $3600,%R8
  cqo
  idivq %R8
  ret


  .globl sec_to_h
sec_to_h:
  movq %RDI,%RAX
  movq $60,%R8
  cqo
  idivq %R8
  ret

  .globl sec_to_s
sec_to_s:
  movq %RDI,%RAX
