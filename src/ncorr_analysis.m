% Script dedicated to NCORR data analysis (Young's Modulus)

% Initializing information
clear all
images = [10,25; 4,5; 9,10; 11,23; 14,21]; % Images within linear elastic region
image_info = ["test00001.csv", "test00002.csv", "test00003.csv", "test00001.csv", "test00005.csv"];
cols = [148,275; 160,252; 171,276; 152,263; 140,245]; % x-axis range of intrest
rows = [14, 257; 74,201; 75,228; 83,314; 78,233]; % y-axis range of intrest



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

    
    
    exx = zeros(1,images(i,2)-images(i,1));
    exy = zeros(1,images(i,2)-images(i,1));
    eyy = zeros(1,images(i,2)-images(i,1));
    
    % Average Srtrain Fields
    for j = images(i,1):images(i,2)
        strainsXX = (data.data_dic_save.strains(j).plot_exx_cur_formatted);
        strainsXY = (data.data_dic_save.strains(j).plot_exy_cur_formatted);
        strainsYY = (data.data_dic_save.strains(j).plot_eyy_cur_formatted);
        exx(j-images(i,1)+1) = average(strainsXX, cols(i,1):cols(i,2), rows(i,1):rows(i,2));
        exy(j-images(i,1)+1) = average(strainsXY, cols(i,1):cols(i,2), rows(i,1):rows(i,2));
        eyy(j-images(i,1)+1) = average(strainsYY, cols(i,1):cols(i,2), rows(i,1):rows(i,2));
       
    end
     poisson = abs(exx(images(i,2)-images(i,1))/eyy(images(i,2)-images(i,1)));

    E = youngsModules(stress, eyy, false);
    fprintf('Youngs Modulus for test %d: %f\n', i, E);
    fprintf('Poisson Raito for test %d: %f\n', i, poisson);
    clear data stress_data image_data image_table t stressXX stressYY stressXY stress;
end

% Find young's modulus
function E = youngsModules(stress, strain, debug)
    LS=fit(strain',stress','poly1');
    if debug
        figure()
        hold on
        scatter(strain, stress)
        plot(LS)
        hold off
    end
    E=LS.p1;
end

% Average data over specific rows and columns
function avg = average(data, rows, cols)
    avg = 0;
    for i = rows
        for j = cols
            avg = avg + data(i,j);
        end
    end
    avg = avg/(length(rows)*length(cols));
end