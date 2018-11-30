module stats
implicit none

contains
    ! psuedorandom numbers with system-dependent seed
    subroutine random_uniform(nval, vals)
        integer :: nval, istat, n
        integer, allocatable :: seed(:)
        real, dimension(nval) :: vals

        ! get psuedorandom numbers
        call random_seed(size=n)
        allocate(seed(n))
        open(15, file='/dev/urandom', access='stream', &
             form='unformatted', action='read', &
             status='old', iostat=istat)
        read(15) seed
        close(15)
        call random_seed(put=seed)
        call random_number(vals)

    end subroutine

    ! psuedorandom numbers that are normal-distributed
    subroutine random_normal(nval, vals)
        integer :: nval
        real, dimension(nval) :: u1, u2, vals
        real :: pi

        pi = 4.*atan(1.)

        ! get uniform psuedorandom numbers and transform to normal
        call random_uniform(nval, u1)
        call random_uniform(nval, u2)
        vals = sqrt(-2.*log(u1))*cos(2.*pi*u2)

    end subroutine
end module
