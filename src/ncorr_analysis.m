% Script dedicated to NCORR data analysis (Young's Modulus)

% Initializing average areas for each specimen
clear all
images = [10,27; 4,8; 4,15; 4,15; 4,15];
image_info = ["test00001.csv", "test00002.csv", "test00003.csv", "test00001.csv", "test00005.csv"];
cols = [148,275; 160,252; 171,276; 147,15; 140,245];
rows = [14, 257; 74,201; 75,228; 61,15; 78,233];



for i = 1:5
    % Load the data
    
    data = load(['./results/NCORR/',num2str(i),'/test',num2str(i),'.mat']);
    stress_data = table2array(readtable(['./results/Data/B',num2str(i),'_parsed','.csv'], 'NumHeaderLines', 1));
    
    image_table = readtable(strcat('./Data/Image Data/',num2str(i),'/',image_info(i)), 'NumHeaderLines', 1);
    image_data = image_table{:, vartype("numeric")};
    % Extract the relevant stresses
    stress = [];

    for j = (images(i,1):images(i,2))
        for k = 1:length(image_data(:,1))
            if image_data(k,1) == j
                t = image_data(k,2);
                break;
            end
        end

        for k = 1:length(stress_data(:,1))
            if stress_data(k,1) <= t && stress_data(k+1,1) > t
                if abs(stress_data(k,1) - t)>= abs(stress_data(k+1,1) - t)
                    stress(j-images(i,1)+1) = stress_data(k,7);
                else
                    stress(j-images(i,1)+1) = stress_data(k+2,7);
                end
                break;
            end
        end
    end

    
    
    exx = zeros(1,images(i,1)-images(i,2));
    exy = zeros(1,images(i,1)-images(i,2));
    eyy = zeros(1,images(i,1)-images(i,2));

    for j = images(i,1):images(i,2)
        strainsXX = (data.data_dic_save.strains(j).plot_exx_cur_formatted);
        strainsXY = (data.data_dic_save.strains(j).plot_exy_cur_formatted);
        strainsYY = (data.data_dic_save.strains(j).plot_eyy_cur_formatted);
        exx(j) = average(strainsXX, cols(i,1):cols(i,2), rows(i,1):rows(i,2));
        exy(j) = average(strainsXY, cols(i,1):cols(i,2), rows(i,1):rows(i,2));
        eyy(j) = average(strainsYY, cols(i,1):cols(i,2), rows(i,1):rows(i,2));
    end
    

    E = youngsModules(stress, eyy);
    fprintf('Youngs Modulus for test %d: %f\n', i, E);
    clear data stress_data image_data image_table t stressXX stressYY stressXY stress;
end

function E = youngsModules(stress, strain)
    idx=find(strain<=0.005,1,'last');
    strain=strain(1:idx);
    stress=stress(1:idx);
    LS=fit(strain',stress','poly1');
    figure()
    hold on
    scatter(strain, stress)
    plot(LS)
    hold off
    E=LS.p1;
end

function avg = average(data, rows, cols)
    avg = 0;
    for i = rows
        for j = cols
            avg = avg + data(i,j);
        end
    end
    avg = avg/(length(rows)*length(cols));
end