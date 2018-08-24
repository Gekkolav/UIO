	.globl hms_to_sec
# Omformer et klokkeslett (angitt i timer, minutter og sekunder) til
# antall sekunder.

hms_to_sec:

	movq	%rdi,%rax  # Hent flytter timer til rax.
	imulq $3600, %rax #Ganger timer med sekunder i rax
	imulq $60, %rsi #Ganger antall minutter med 60
	addq  %rsi, %rax #Legger til sekunder fra minutter
	addq  %rdx, %rax #Legger til sekunder

	ret


	.globl	sec_to_h
# Gitt et tidspunkt (angitt som sekunder siden midnatt), finn timen.

sec_to_h:

	movq %RDI,%RAX #Flytter antall sekunder til rax
	movq $3600,%R8 #flyyter 3600 til R8
	cqo
	idivq %R8 #Deler sekunder på 3600
	ret

	ret


	.globl	sec_to_s
# Gitt et tidspunkt (angitt som sekunder siden midnatt), finn sekundet.

sec_to_s:

	movq %RDI,%RAX # flytter innput til rax
	movq $3600,%R8
	movq $60,%R9 #Legger inn de to variablene
	cqo
	idivq %R8 #Finner først antall timer
	movq %rdx,%rax #Flytter resten
	cqo
	idivq %R9 #Finner antall minutter
	movq %rdx, %rax #Resten bli da svaret

	ret


	.globl	sec_to_m
# Gitt et tidspunkt (angitt som sekunder siden midnatt), finn minuttet.

sec_to_m:

	movq %RDI,%RAX #Flytter input
	movq $3600,%R8
	movq $60,%R9 #Legger inn variablene
	cqo
	idivq %R8 #Finner antall timer
	movq %rdx,%rax
	cqo
	idivq %R9 #Finner minutter

	ret
