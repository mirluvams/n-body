// Author: Victor De la Luz
// vdelaluz@enesmorelia.unam.mx
// GNU/GPL

#include <stdio.h>
#include <stdlib.h>

#include "numeric.h"
#include "model.h"
#include "particle.h"

//MKS system

int main(int argn, char **args){
    srand(time(0));
    int N; sscanf_s(args[1],"%d", &N);
    printf("%d\n", N);
    double M; sscanf_s(args[2],"%lf", &M);
    printf("%lf\n", M);
    double VMax; sscanf_s(args[3],"%lf", &VMax);
    double total_mass; sscanf_s(args[4],"%lf", &total_mass);
	
    Model model = new_Model("System", N);
    Integrator integrator = new_integrator(1, 1.0);
    for (int i = 0; i < N; i++) {
        double x, y, z;
        double vx, vy, vz;
        x = ((double)rand() / (double)RAND_MAX) * M - M / 2;
        y = ((double)rand() / (double)RAND_MAX) * M - M / 2;
        z = ((double)rand() / (double)RAND_MAX) * M - M / 2;
        vx = (double)rand() / (double)RAND_MAX * VMax;
        vy = (double)rand() / (double)RAND_MAX * VMax;
        vz = (double)rand() / (double)RAND_MAX * VMax;
        Particle particle = new_Particle(total_mass, x, y, z, vx, vy, vz);
        add_Particle_to_Model(&model, particle);
    }


    for (int i = 0; i < 5000; i++) {
        if ((i % 50) == 0) {
            printf("#%i\n", i);
            print_Model(model);
        }
        model = integrator_solve(integrator, model);
    }

    return 0;
}
