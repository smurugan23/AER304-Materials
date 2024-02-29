% Script dedicated to NCORR data analysis (Young's Modulus)

% Initializing average areas for each specimen
areas = [47.687, 47.322, 47.223, 50.836, 49.489];
strain_im = [5:10



for i = 1:5
    % Load the data
    load(['./results/NCORR/',num2str(i),'/test',num2str(i),'.mat']);
    



    E = 0;
    fprintf('Youngs Modulus for test %d: %f\n', i, E);
end

function E = youngsModules(stress, strain)
    E = stress/strain;
end

function avg = average(data, row, cols)
    data = 0

    for i = rows
        for j = cols
            avg = avg + data(i,j);
        end
    end
    avg = avg/(length(rows)*length(cols));
end