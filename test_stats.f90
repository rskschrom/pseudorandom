program test_stats
use stats
implicit none

    integer, parameter :: nval = 100001
    integer :: i
    real, dimension(nval) :: rv

    ! test normal distribution sampling
    call random_normal(nval, rv)
    open(11, file='test_stats.txt')
    do i = 1, nval
        write(11, *) rv(i)
    enddo
    close(11)

end program
